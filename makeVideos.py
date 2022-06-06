from downloader import *
import os 
import cv2 
from PIL import Image 
from django.conf import settings
import urllib.request
from gtts import gTTS,tts
import shutil
from moviepy.editor import *
import settings
from vakyansh_translation_hindi_audio import *
import glob
import math
import numpy
import random

def concatenate_audio_moviepy(audio_clip_path, output_path):
    pauseDuration = '80' #in millisecond
    audio_clip_path = glob.glob(audio_clip_path)
    print(audio_clip_path)
    clips = [AudioFileClip(c) for c in audio_clip_path]
    mutedClip = clips[0].fx( afx.volumex, 0.0).subclip('00:00:00.00', '00:00:00.' + pauseDuration)
    clipsAfterAddingPause = []
    for clip in clips:
        clipsAfterAddingPause.append(clip)
        clipsAfterAddingPause.append(mutedClip)
    final_clip = concatenate_audioclips(clipsAfterAddingPause)
    final_clip.write_audiofile(output_path, verbose= False, logger= None)
    print("Audio Concatenated Successfully")

def makeAudio(name,content):
    try:
        currentAudioIndex = 0 #to track audio file name    
        text_in_list = content.split('.')
        for textaf in text_in_list:
            textaf = textaf + "." #To add period
            try:
                os.chdir(os.path.join(settings.BASE_DIR, r"dataset/"+name))
                filepathtosave = os.path.join(os.path.join(settings.BASE_DIR, r"dataset/"+name), "audio" + str(currentAudioIndex) + ".mp3") # with audio.mp3 appended            
                sr,ttsG_audio = run_tts(textaf,'hi', filepathtosave)
                print("Audio Generated")
                #ttsG_audio.save('audio.mp3')
            except Exception as e:
                print(e)
                return False
            currentAudioIndex = currentAudioIndex + 1
        concatenate_audio_moviepy(os.path.join(settings.BASE_DIR, r"dataset/"+name + r"/audio*"), os.path.join(os.path.join(settings.BASE_DIR, r"dataset/"+name), "audio.mp3"))
        return True
    except Exception as e: 
        print('m.v. makeaudio')
        print(e)

def downloadImages(title):
    try:
        # title.replace(' ','-')
        os.chdir(os.path.join(settings.BASE_DIR,''))
        download(title, limit=10,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=300)
    except:
        print('m.v. downloadimages')


def makeVideo(name,content):
    try:
        print(os.path.isdir(os.path.join(settings.BASE_DIR, r"dataset/"+name)))
        if os.path.isdir(os.path.join(settings.BASE_DIR, r"dataset/"+name)):
            shutil.rmtree(os.path.join(settings.BASE_DIR, r"dataset/"+name))
        downloadImages(name)
        status = makeAudio(name,content)
        if not status:
            return 'GTTS ERR'
        
        print(os.getcwd()) 

        os.chdir(os.path.join(settings.BASE_DIR, r"dataset/"+name)) 
        path = os.path.join(settings.BASE_DIR, r"dataset/"+name)

        mean_height = 1080
        mean_width = 1920

        num_of_images = len(os.listdir('.')) 

        # for file in os.listdir('.'): 
        #     if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
        #         im = Image.open(os.path.join(path, file)) 
        #         width, height = im.size 
        #         mean_width += width 
        #         mean_height += height 

        # mean_width = int(mean_width / num_of_images) 
        # mean_height = int(mean_height / num_of_images) 

        for file in os.listdir('.'): 
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
                # opening image using PIL Image 
                im = Image.open(os.path.join(path, file)).convert('RGB')

                # im.size includes the height and width of image 
                width, height = im.size 
                print(width, height) 

                # resizing 
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS) 
                imResize.save( file, 'JPEG', quality = 95) # setting quality 

        generate_video_from_moviepy(name) 

        print('Video Generated')

        addAudioToVideo(name)
        
        return os.path.join(settings.BASE_DIR, r"dataset/"+name+r'/'+name+r'.mp4')
    except Exception as e:
        print(e)

def zoom_in_effect(clip, zoom_ratio=0.04):
    def effect(get_frame, t):
        img = Image.fromarray(get_frame(t))
        base_size = img.size

        new_size = [
            math.ceil(img.size[0] * (1 + (zoom_ratio * t))),
            math.ceil(img.size[1] * (1 + (zoom_ratio * t)))
        ]

        # The new dimensions must be even.
        new_size[0] = new_size[0] + (new_size[0] % 2)
        new_size[1] = new_size[1] + (new_size[1] % 2)

        img = img.resize(new_size, Image.LANCZOS)

        x = math.ceil((new_size[0] - base_size[0]) / 2)
        y = math.ceil((new_size[1] - base_size[1]) / 2)

        img = img.crop([
            x, y, new_size[0] - x, new_size[1] - y
        ]).resize(base_size, Image.LANCZOS)

        result = numpy.array(img)
        img.close()

        return result

    return clip.fl(effect)

def slide_fade_effect(slides):
    padding = 2
    clips = []
    clips.append(slides[0])
    idx = slides[0].duration - padding
    for index, slide in enumerate(slides):
        if (index % 6 != 0) or True: #True always till found the reason to why screen gets blank
            clips.append(slide.set_start(idx).crossfadein(padding))
        else:
            clips.append(slide.fx( transfx.slide_out, 1, 'bottom'))

        idx += slide.duration - padding
    
    final_video = CompositeVideoClip(clips)
    
    return final_video
    
def generate_video_from_moviepy(name):
    try:
        size = (1920, 1080)

        image_folder = '.' # make sure to use your folder 
        video_name = 'mygeneratedvideo.mp4'
        os.chdir(os.path.join(settings.BASE_DIR, r"dataset/"+name))
        print(os.listdir())
        images = [img for img in os.listdir(image_folder) 
        if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]
        
        #Total video length will be setduration * num of images
        audioLength = AudioFileClip('audio.mp3').duration
        durationofoneclip = 5 #set_duration
        videoToLoop = int((audioLength / (len(images) * durationofoneclip)) + 1)
        
        for itertator in range(videoToLoop):
            images = images + images

        slides = []
        for n, url in enumerate(images):
            slides.append(
                ImageClip(url).set_fps(25).set_duration(durationofoneclip).resize(size)
            )

            slides[n] = zoom_in_effect(slides[n], 0.04)

        video = slide_fade_effect(slides)
        #video = concatenate_videoclips(slides)
        video.write_videofile(video_name, verbose= False, logger= None)
        print("Video Generated from Moviepy before Audio Successfully")
    except Exception as e:
        print(e)

# Video Generating function 
def generate_video(name):
    try:
        image_folder = '.' # make sure to use your folder 
        video_name = 'mygeneratedvideo.mp4'
        os.chdir(os.path.join(settings.BASE_DIR, r"dataset/"+name))
        print(os.listdir())
        images = [img for img in os.listdir(image_folder) 
        if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]
    

        frame = cv2.imread(os.path.join(image_folder, images[0])) 

        height, width, layers = frame.shape
        frameRate=10
        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height)) 
        audioLength = AudioFileClip('audio.mp3').duration

        videoToLoop = audioLength
        if videoToLoop <1:
            videoToLoop = 1

        # Appending the images to the video one by one 
        while videoToLoop > 0:
            for image in images:
                for i in range(frameRate):
                    video.write(cv2.imread(os.path.join(image_folder, image)))
            videoToLoop-=(frameRate*len(images))
        # Deallocating memories taken for window creation 
        cv2.destroyAllWindows()
        video.release() # releasing the video generated 
        print(os.listdir())
    except Exception as e:
        print('m.v. generatevideo')
        print(e)
    
        
def addAudioToVideo(name):
    try:
        os.chdir(os.path.join(settings.BASE_DIR, r"RequiredFiles/"))
        bgAudio = AudioFileClip('bgAudioEntertainment.mp3')
        bgAudio = bgAudio.fx(afx.volumex, 0.1)
        os.chdir(os.path.join(settings.BASE_DIR, r"dataset/"+name))
        print(os.listdir())
        audiofile = AudioFileClip('audio.mp3')
        audioFileDuration = audiofile.duration
        videoclip = VideoFileClip("mygeneratedvideo.mp4")
        audiofile = CompositeAudioClip([audiofile, bgAudio])
        videoclip = videoclip.set_audio(audiofile)
        # videoclip.audio = new_audioclip
        videoclip = videoclip.subclip(0, audioFileDuration)
        #videoclip = videoclip.speedx(factor=1.1)
        # videoclip = videoclip.fx(speedx, 1.3)
        os.chdir(os.path.join(settings.BASE_DIR, ""))
        videoclip.write_videofile("final"+".mp4", verbose= False, logger= None)
        print("Video Generated Successfully")
    except Exception as e:
        print('addaudioto video m.v.')
        print(e)
