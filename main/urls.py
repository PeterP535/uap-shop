from django.urls import path
from main.views import show_main, create_product, edit_product, delete_product, add_to_cart_form, edit_cart_item, show_xml, show_json, show_xml_by_id, show_json_by_id, login_user, logout_user, delete_cart_item, register, add_game_ajax


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('edit-product/<str:product_id>/', edit_product, name='edit_product'),
    path('delete-product/<str:product_id>/', delete_product, name='delete_product'),
    path('add-to-cart/<str:game_id>/', add_to_cart_form, name='add_to_cart_form'),
    path('edit-cart-item/<int:item_id>/', edit_cart_item, name='edit_cart_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-cart-item/<int:item_id>/', delete_cart_item, name='delete_cart_item'),  
    path('register/', register, name='register'),
    path('add-game-ajax/', add_game_ajax, name='add_game_ajax'),
]
