import json
import logging

def read_file():
    try:
        with open('posts.json', encoding='utf-8') as f:
            text = json.load(f)
        return text
    except:
        logging.info('error')
        return []


def search(s):
    post = []
    for i in read_file():
        print(i)
        if s.lower() in i["content"].lower():
            post.append(i)
    print(post)
    return post


def save_photo(picture):
    filename = picture.filename
    path = f"./uploads/images/{filename}"
    picture.save(path)
    return path


def save_post(post):
    posts = read_file()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f)
    return post
