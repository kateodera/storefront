from pickle import TRUE
from urllib import response
from store.models import Collection, Product
from rest_framework import status
import pytest
from model_bakery import baker


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/',collection)
    return do_create_collection

@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_not_anonymous_return_401(self, api_client, create_collection):
        response = create_collection({'title':'a' })

        assert response.status_code != status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_is_not_admin_return_403(self, api_client, create_collection, authenticate_user):
        authenticate_user()
        response = create_collection({'title':'a' })

        assert response.status_code != status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, api_client, create_collection, authenticate_user):
        authenticate_user(is_staff = True)
        response = create_collection({'title':'' })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_return_201(self, api_client, create_collection, authenticate_user):
        authenticate_user(is_staff = True)
        response = create_collection({'title':'a' })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        collection = baker.make(Collection)
        response = api_client.get(f'/store/collections/{collection.id}/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title' : collection.title,
            'products_count': 0   
             }


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_not_anonymous_return_401(self, api_client, create_product):
        response = create_product({'title':'b' })

        assert response.status_code != status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_is_not_admin_return_403(self, api_client, create_product, authenticate_user):
        authenticate_user()
        response = create_product({'title':'b' })

        assert response.status_code != status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, api_client, create_product, authenticate_user):
        authenticate_user(is_staff = True)
        response = create_product({'title':'' })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_return_201(self, api_client, create_product, authenticate_user):
        authenticate_user(is_staff = True)
        response = create_product({'title':'b' })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_data_exists_returns_200(self, api_client):
        product = baker.make(Product)
        response = api_client.get(f'/store/products/{product.id}/')
        
        assert response.status_code == status.HTTP_200_OK