import sys
import os
from tinytag import TinyTag
from itertools import groupby


def get_args():
    """
        artist_name = sys.argv[1]
    """
    return sys.argv[1]


def get_mp3_files(directory_path):
    for root, dirs, filenames in os.walk(directory_path, topdown=True):
        for filename in filenames:
            if filename.endswith('.mp3'):
                yield os.path.abspath(os.path.join(root, filename))


def create_music_collection(mp3_files):
    collection = []
    for mp3_file in mp3_files:
        collection.append([mp3_file, TinyTag.get(mp3_file)])
    return collection


def filter_collection_by_criteria(collection, criteria):
    return [
        [_path, tags]
        for _path, tags in collection
        if tags.artist == criteria
    ]


def group_collection_by_album(collection):
    for group, items in groupby(collection, key=lambda item: item[1].album):
        yield group, list(items)


def pretty_print(_grouped_collection):
    for album, files in _grouped_collection:
        print(album)
        for file_counter, [_path, tags] in enumerate(files, 1):
            print('{:<4}{}. "{}" {} ({})'.format(
                ' ',
                file_counter,
                tags.title,
                beatufy_duration(tags.duration),
                _path))


def beatufy_duration(duration):
    minutes = duration / 60
    seconds = duration % 60
    return '{}:{}'.format(str(minutes)[:1], str(seconds)[:2])


if __name__ == '__main__':
    artist = get_args()
    path = 'music'
    mp3_collection = create_music_collection(get_mp3_files(path))
    if not mp3_collection:
        exit('No mp3 files found')
    filtered_collection = filter_collection_by_criteria(mp3_collection, artist)
    grouped_collection = group_collection_by_album(filtered_collection)
    pretty_print(grouped_collection)
