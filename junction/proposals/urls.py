from django.conf.urls import patterns, url

from proposals.views import create_proposal, list_proposals, update_proposal, detail_proposal, delete_proposal


urlpatterns = patterns('',
    url(r'^$', list_proposals, name='proposals-list'),
    url(r'^create/$', create_proposal, name='proposal-create'),
    url(r'^update/(?P<proposal_id>\d+)/$', update_proposal, name='proposal-update'),  # TODO: Slug based
    url(r'^proposal/(?P<proposal_id>\d+)/$', detail_proposal, name='proposal-detail'),  # TODO: Slug based
    url(r'^delete/(?P<proposal_id>\d+)/$', delete_proposal, name='proposal-delete'),
)
