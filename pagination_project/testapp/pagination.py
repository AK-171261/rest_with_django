from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "MyPage"  # by default name is page it can be override to anyname here MyPage we used
    page_size_query_param = "page_size"  # means per page this much result we need,http://localhost:8000/api/?mypage=7&num=13
    max_page_size = 15  # max nos of record will be displayed this much only
    last_page_strings = ('endpage',)  # default value is ('last',)


class MyPagination2(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = "mylimit"
    offset_query_param = "myoffset"
    max_limit = 20


class MyPagination3(CursorPagination):
    ordering = 'esal'
    page_size = 5