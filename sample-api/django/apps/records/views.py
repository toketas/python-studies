from rest_framework.response import Response
from rest_framework.decorators import api_view

from helpers.logging import log
from .models import Record
from .serializers import RecordSerializer


@api_view(["GET"])
def getRecords(request):
    import logging
    logger = logging.getLogger("api")
    logger.info("loggingggg")
    logger.info("Retrieving all records...")

    records = Record.objects.all()
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addRecord(request):
    serializer = RecordSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
