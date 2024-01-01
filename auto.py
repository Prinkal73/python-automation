import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def seperate_and_move(directory_path,file_path):
    # create directory if they don't exists
    image_directory = os.path.join(directory_path, 'All photos')
    vid_directory = os.path.join(directory_path, 'All videos')
    docs_directory = os.path.join(directory_path, 'All documents')
    apps_directory = os.path.join(directory_path, 'All Aplication')
    zip_directory = os.path.join(directory_path, 'All zip files')
    song_directory = os.path.join(directory_path, 'All songs')
    others_directory = os.path.join(directory_path, 'Others')
    
    # by checking exist_ok = True I'm making sure that if the directory already exists it won't raise an error
    os.makedirs(image_directory, exist_ok=True)
    os.makedirs(vid_directory, exist_ok=True)
    os.makedirs(docs_directory, exist_ok=True)
    os.makedirs(apps_directory, exist_ok=True)
    os.makedirs(zip_directory, exist_ok=True)
    os.makedirs(song_directory, exist_ok=True)
    os.makedirs(others_directory, exist_ok=True)
    
    with os.scandir(directory_path) as entries:
        for entry in entries:
            if entry.is_file():
                file_name = entry.name
                source_path = entry.path
                if file_name.lower().endswith(('.jpg' , '.png' , '.jpeg','.webp','.raw','.psd','.jp2')):
                    destination_path = os.path.join(image_directory, file_name)
                elif file_name.lower().endswith(('.mp4','.mkv','.wmv','.m4v')):
                    destination_path = os.path.join(vid_directory, file_name)
                elif file_name.lower().endswith(('.doc','.docx','.pdf','.odt','.txt','.ppt','.pptx','.csv')):
                    destination_path = os.path.join(docs_directory, file_name)
                elif file_name.lower().endswith(('.exe','.apk','.app','.ipa','.jar','.dmg','.msi','.deb','.rpm')):
                    destination_path = os.path.join(apps_directory, file_name)
                elif file_name.lower().endswith(('.zip','.tar.gz','.tgz')):
                    destination_path = os.path.join(zip_directory, file_name)
                elif file_name.lower().endswith(('.mp3','.wav','.m4a','.ape','.mid','.midi')):
                    destination_path = os.path.join(song_directory, file_name)
                else:
                    destination_path = os.path.join(others_directory, file_name)
                try:
                    shutil.move(source_path,destination_path)
                except (shutil.Error, PermissionError):
                    print(f'failed to move {source_path} to {destination_path}')
                    


# if __name__ == "__main__":
    # directory_path = '/Users/prink/Downloads'
#     seperate_and_move(directory_path)
directory_path = '/Users/prink/Downloads'


def monitor_directory(directory_path):
    class MyHandler(FileSystemEventHandler):
        def on_created(self, event):
            if not event.is_directory:
                file_path = event.src_path
                seperate_and_move(directory_path,file_path)

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()
    print(f'Monitoring directory: {directory_path}')

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    directory_path = '/Users/prink/Downloads'
    # seperate_and_move(directory_path)
    monitor_directory(directory_path)