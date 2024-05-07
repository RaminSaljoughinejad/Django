from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug":"neural-networks-beginners",
        "image": "angry_green_avatar.webp",
        "author": "Ramin Saljoughinejad",
        "date": date(2023, 4, 5),
        "title" : "Neural Networks For Beginners",
        "excerpt": "6This Course is for complete beginners. You know need some basic knowledge in Python and nothing else.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aut inventore doloremque repellat tempora debitis delectus ullam, nemo consectetur ex?
        Ipsa sit deleniti non labore cupiditate earum debitis, quos unde nisi."""
    },
    {
        "slug":"Python-beginners",
        "image": "sad_green_avatar.jpg",
        "author": "Ramin Saljoughinejad",
        "date": date(2020, 2, 6),
        "title" : "Python For Beginners",
        "excerpt": "5This Course is for complete beginners. You know need some basic knowledge in Python and nothing else.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aut inventore doloremque repellat tempora debitis delectus ullam, nemo consectetur ex?
        Ipsa sit deleniti non labore cupiditate earum debitis, quos unde nisi."""
    },
    {
        "slug":"Python-advanced",
        "image": "purple_avatar.webp",
        "author": "Ramin Saljoughinejad",
        "date": date(2021, 9, 8),
        "title" : "Advanced Topics in Python",
        "excerpt": "4This Course is for complete beginners. You know need some basic knowledge in Python and nothing else.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aut inventore doloremque repellat tempora debitis delectus ullam, nemo consectetur ex?
        Ipsa sit deleniti non labore cupiditate earum debitis, quos unde nisi."""
    },
    {
        "slug":"neural-networks-advanced",
        "image": "orange_avatar.jpg",
        "author": "Ramin Saljoughinejad",
        "date": date(2022, 2, 5),
        "title" : "Advanced Neural Networks",
        "excerpt": "3This Course is for complete beginners. You know need some basic knowledge in Python and nothing else.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aut inventore doloremque repellat tempora debitis delectus ullam, nemo consectetur ex?
        Ipsa sit deleniti non labore cupiditate earum debitis, quos unde nisi."""
    },
    {
        "slug":"web-design-beginners",
        "image": "blue_green_avatar.jpg",
        "author": "Ramin Saljoughinejad",
        "date": date(2023, 1, 1),
        "title" : "Web Design 101",
        "excerpt": "2This Course is for complete beginners. You know need some basic knowledge in Python and nothing else.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aut inventore doloremque repellat tempora debitis delectus ullam, nemo consectetur ex?
        Ipsa sit deleniti non labore cupiditate earum debitis, quos unde nisi."""
    },
    {
        "slug":"Django-full-course",
        "image": "avatar.jpg",
        "author": "Ramin Saljoughinejad",
        "date": date(2024, 7, 1),
        "title" : "Django Framework",
        "excerpt": "1This Course is for complete beginners. You know need some basic knowledge in Python and nothing else.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aut inventore doloremque repellat tempora debitis delectus ullam, nemo consectetur ex?
        Ipsa sit deleniti non labore cupiditate earum debitis, quos unde nisi."""
    }
]


def get_date(post):
    return post['date']

def index(request):
    soreted_posts = sorted(all_posts, key=get_date)
    latest_posts = soreted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts":latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html", {
        "post":post
    }) 