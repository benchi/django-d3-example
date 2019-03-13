from django.conf.urls import url


from .views import graph, play_count_by_month, mock_data

urlpatterns = [
    url(r'^$', graph),
    url(r'^api/play_count_by_month', play_count_by_month, name='play_count_by_month'),
    url(r'^api/mock_data', mock_data, name='mock_data'),
]
