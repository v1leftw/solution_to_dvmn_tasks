import sys
import os
from tinytag import TinyTag


def get_args():
    return sys.argv[1]


def get_mp3_files(directory_path):
    for root, dirs, filenames in os.walk(directory_path, topdown=True):
        for filename in filenames:
            if filename.endswith(".mp3"):
                yield os.path.abspath(os.path.join(root, filename))


def get_tags(path_to_mp3_file):
    tags = TinyTag.get(path_to_mp3_file)
    return tags


def create_music_collection(directory_path):
    collection = []
    for mp3_file_path in get_mp3_files(directory_path):
        collection.append([mp3_file_path, get_tags(mp3_file_path)])
    print(type(collection))
    return collection


def sort_music_collection_by_artist_name(artist_name, collection):
    for _path, tags in collection:
        print(tags.artist)


if __name__ == '__main__':
    artist = get_args()
    path = "music"
    sort_music_collection_by_artist_name(artist, create_music_collection(path))
