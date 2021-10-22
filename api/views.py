import numpy as np
from .apps import ApiConfig
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

response_schema = {
    '200': openapi.Response(
        description='Returns Prediction API calculated probability',
    ),
}

class ReturnsAPI(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'dp': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'dy': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'ep': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'de': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'svar': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'bm': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'ntis': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'tbl': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'lty': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'ltr': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'tms': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'dfy': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'dfr': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
            'infl': openapi.Schema(type=openapi.TYPE_NUMBER,format=openapi.FORMAT_DOUBLE),
        }),
        responses=response_schema)

    def post(self, request):
        float_features = [float(x) for x in request.data.values()]
        final_features = [np.array(float_features)]
        log_reg_model = ApiConfig.model
        prediction = (log_reg_model.predict(final_features)).astype(int)
        return Response('Your RETURNS probability is {}'.format(prediction), status=status.HTTP_200_OK)
