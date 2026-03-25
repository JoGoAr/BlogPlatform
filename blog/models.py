from django.db import models
from django.utils import timezone

class Post(models.Model):
    """Represents a single blog post."""
    title = models.CharField(max_length=200, help_text="The headline of the post")
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="URL-friendly version of the title")
    content = models.TextField(help_text="The main body of the post")
    author = models.CharField(max_length=100, help_text="Name of the author")
    created_at = models.DateTimeField(default=timezone.now, help_text="When the post was created")
    published = models.BooleanField(default=False, help_text="Is this post visible to the public?")

    class Meta:
        ordering = ['-created_at']  # Newest posts first

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)