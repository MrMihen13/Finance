# TODO Написать краткое описание для каждого класса и функции

from rest_framework import pagination, response, status
from rest_framework.exceptions import NotFound


class CustomPagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data, next_month=None, prev_month=None):
        if next_month is not None and prev_month is not None:
            return response.Response({
                'links': {
                    'next_page': self.get_next_link(),
                    'prev_page': self.get_previous_link(),
                    'next_month': next_month,
                    'prev_month': prev_month,
                },
                'count': self.page.paginator.count,
                'results': data
            }, status=status.HTTP_200_OK)
        else:
            return response.Response({
                'links': {
                    'next_page': self.get_next_link(),
                    'prev_page': self.get_previous_link(),
                },
                'count': self.page.paginator.count,
                'results': data
            }, status=status.HTTP_200_OK)
