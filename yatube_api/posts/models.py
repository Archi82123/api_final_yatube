from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст поста',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата',
        help_text='Дата добавления',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        help_text='Автор поста',
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост',
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='posts/images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.text[:15]


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Название группы',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='URL',
        help_text='Адрес url группы',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание группы',
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
        help_text='Пост к которому оставлен комментарий',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Автор комментария',
    )
    text = models.TextField(
        verbose_name='Комментарий',
        help_text='Текст комментария',
        max_length=500,
    )
    created = models.DateTimeField(
        verbose_name='Дата',
        help_text='Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        help_text='Пользователь, который подписывается на авторов',
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
        verbose_name='Автор',
        help_text='Автор, на которого подписываются',
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('user', 'following'),
                                    name='unique_follow'),
        )

    def __str__(self):
        return f"Автор: {self.following}, подписчик: {self.user}"
