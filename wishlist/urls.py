from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_xml, show_wishlist_json, show_wishlist_ajax, show_item_by_id_xml, show_item_by_id_json, register, login_user, logout_user, add_barang

app_name = 'wishlist'

urlpatterns = [
	path('', show_wishlist, name='show_wishlist'),
	path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
	path('ajax/submit', add_barang, name='add_barang'),
	path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
	path('json/', show_wishlist_json, name='show_wishlist_json'),
	path('xml/<int:id>', show_item_by_id_xml, name='show_item_by_id_xml'),
	path('json/<int:id>', show_item_by_id_json, name='show_item_by_id_json'),
	path('register/', register, name='register'),
	path('login/', login_user, name='login'),
	path('logout/', logout_user, name='logout'),
]