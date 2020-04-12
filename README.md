# Python Django Rest Api

#### Installation 


#### Start App

```
python manage.py startapp api
```
Now add this to your `settings.py's` `INSTALLED_APPS` section

#### Create super user
```
python manage.py createsuperuser
```



## Models 
Creating a article model in your `models.py` file
```
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

```
* Make migrations from the above model `python3 manage.py makemigrations`
* Migrate `python3 manage.py migrate`
* Add this model to your `admin.py` in order to access through your administration panel. `from .models import Article` and register it `admin.site.register(Article)`.


## Serializer Class

Before sending data to client we need to serialize it to json. Api communication is always in json.

```
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

```

## Model Serializer




## Python Shell Django
```
python3 manage.py shell
```

**Example Shell Serialization Check**
```
>>> from api.models import Article

>>> from api.serializers import ArticleSerializer

>>> from rest_framework.renderers import JSONRenderer

>>> from rest_framework.parsers import JSONParser

>>> a = Article(title='Article Title',author='Selvesan',email='dev.selvesan@gmail.com')

>>> a.save()

>>> a = Article(title='Cool Gugles',author='Google',email='selvesanxy@gmail.com')

>>> a.save()

>>> serializedArticle = ArticleSerializer(a)

>>> serializedArticle.data
{'title': 'Cool Gugles', 'author': 'Google', 'email': 'selvesanxy@gmail.com', 'date': '2020-04-12T04:09:48.037458Z'}

>>> content = JSONRenderer().render(serializedArticle.data)

>>> content
b'{"title":"Cool Gugles","author":"Google","email":"selvesanxy@gmail.com","date":"2020-04-12T04:09:48.037458Z"}'

>> serializeMany=ArticleSerializer(Article.objects.all(),many=True)

>> serializeMany.data

```



### Api Decorator Views
```
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = ArticleSerializer(data=data)
        serializer = ArticleSerializer(data=request.data, status=status.HTTP_201_CREATED)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```


## Django Rest Framework

Add `rest_framework` to your `settings.py's ` `INSTALLED_APPS`

