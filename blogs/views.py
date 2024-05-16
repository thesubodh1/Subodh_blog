from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "mountains.jpg",
        "author" : "Subodh",
        "date" : date(2024,5,16),
        "title" : "Mountain Hiking",
        "excerpt" : "Theres nothing like the views you get when hiking in the mountain, i wasnt even prepared about how was about to happen",
        "content" : """
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec urna at 
                        nunc varius bibendum. Aliquam erat volutpat. Praesent fringilla, arcu nec 
                        ullamcorper vehicula, felis sapien tincidunt lectus, sed gravida tortor sapien 
                        et ligula.

                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec urna at 
                        nunc varius bibendum. Aliquam erat volutpat. Praesent fringilla, arcu nec 
                        ullamcorper vehicula, felis sapien tincidunt lectus, sed gravida tortor sapien 
                        et ligula.

                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec urna at 
                        nunc varius bibendum. Aliquam erat volutpat. Praesent fringilla, arcu nec 
                        ullamcorper vehicula, felis sapien tincidunt lectus, sed gravida tortor sapien 
                        et ligula.

                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec urna at 
                        nunc varius bibendum. Aliquam erat volutpat. Praesent fringilla, arcu nec 
                        ullamcorper vehicula, felis sapien tincidunt lectus, sed gravida tortor sapien 
                        et ligula.
                    """
    },
     {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]
def get_date(post):
    return post['date']



def index(request):
    sorted_post = sorted(all_posts,key=get_date)
    leatest_post = sorted_post[-3:]
    return render(request,"blogs/index.html",{
        "posts" : leatest_post,
    })

def posts(request):
    return render(request,"blogs/all-post.html",{
        "all_posts" : all_posts,
    })

def post(request,slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blogs/post-detail.html",{
        "one_post" : post,
    })