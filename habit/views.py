
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.permissions import AllowAny

from habit.models import Habit
from habit.paginations import CustomPagination
from habit.permissions import IsCreator
from habit.serializers import HabitSerializer


class HabitListApiView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (AllowAny,)  # Возможно строка не нужна, ведь IsAuthenticated присутствует в settings.py

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        elif user.is_authenticated:
            return Habit.objects.filter(creator=user)
        return Habit.objects.all()


class HabitIsPublishedListApiView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)  # Возможно строка не нужна, ведь IsAuthenticated присутствует в settings.py

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        elif self.request.user.is_authenticated:
            return Habit.objects.filter(is_published=True) | Habit.objects.filter(creator=user)

        return Habit.objects.all()


class HabitCreateApiView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)  # Возможно строка не нужна, ведь IsAuthenticated присутствует в settings.py

    def perform_create(self, serializer):
        """ Делаем текущего пользователя 'Создателем' привычки. """
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        new_habit.save()


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsCreator,)


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsCreator,)
