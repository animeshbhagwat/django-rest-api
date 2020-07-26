from universityapi.viewsets import UniversityViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('univeristy', UniversityViewset, basename='ln-languages')

