def shipping_label(*args,**kwargs):
    # for key,values in kwargs.items():
    #     print(f"{key}:{values}")
    print(f"{kwargs.get('colony')}")
    for a in kwargs:
        print(kwargs[a])
shipping_label("Sanidhya Pal","2nd year Btech",colony="sangam nagar",city="indore",state="MP")