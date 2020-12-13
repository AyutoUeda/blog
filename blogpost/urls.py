from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('list/', BlogList.as_view()),
    path('detail/<int:pk>/', BlogDetail.as_view())
]

# <int:pk>/ はテーブルに入っているデータを具体的に指定する上で使われるコード
# intはintegerの略であり、整数型のあることを明示する
# pkはprimary keyの略。データベースがデータを特定するときに使われる項目のことを意味する。
# blogpost/migrations/0002_blogmodel.py を参照