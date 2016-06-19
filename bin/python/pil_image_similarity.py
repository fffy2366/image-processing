#sudo pip install PIL
def pil_image_similarity(filepath1, filepath2):
    from PIL import Image
    import math
    import operator

    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)

#    image1 = get_thumbnail(img1)
#    image2 = get_thumbnail(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms

print pil_image_similarity('/Users/fengxuting/Downloads/1464316500603A166E32.jpg',
                           '/Users/fengxuting/Downloads/1464319730080A44844B.jpg')