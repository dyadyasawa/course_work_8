
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginations import CustomPagination
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


class HabitListApiView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)  # Возможно строка не нужна, ведь IsAuthenticated присутствует в settings.py

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Habit.objects.filter(user=user)
        return Habit.objects.all()


class HabitIsPublishedListApiView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)  # Возможно строка не нужна, ведь IsAuthenticated присутствует в settings.py


class HabitCreateApiView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)  # Возможно строка не нужна, ведь IsAuthenticated присутствует в settings.py

    def perform_create(self, serializer):
        """ Делаем текущего пользователя 'Создателем' привычки. """
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)
