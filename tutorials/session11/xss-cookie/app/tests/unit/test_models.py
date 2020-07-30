import pytest


def test_save_post_sets_id():
    from xss_demo.models import (
        DB,
        Post,
        )

    post = Post('Post 1', 'Just some text', 'admin')
    assert post.id is None
    DB.save(post)
    assert post.id is not None


def test_get_post_returns_same_data():
    from xss_demo.models import (
        DB,
        Post,
        )

    post = Post('Post 1', 'Just some text', 'admin')
    DB.save(post)
    post2 = DB.get(Post, post.id)
    assert post is not post2  # different objects
    assert post.__dict__ == post2.__dict__


def test_get_post_invalid_id():
    from xss_demo.models import (
        DB,
        Post,
        )

    with pytest.raises(ValueError):
        DB.get(Post, 99)


def test_save_existing_post_writes_data():
    from xss_demo.models import (
        DB,
        Post,
        )

    post = Post('Post 1', 'Just some text', 'admin')
    DB.save(post)
    original_id = post.id
    post.content = 'Modified text'
    DB.save(post)
    assert post.id == original_id
    assert DB.get(Post, original_id).content == 'Modified text'


def test_save_post_invalid_id():
    from xss_demo.models import (
        DB,
        Post,
        )

    post = Post('Post 1', 'Just some text', 'admin')
    post.id = 99
    with pytest.raises(ValueError):
        DB.save(post)


def test_delete_post():
    from xss_demo.models import (
        DB,
        Post,
        )

    post = Post('Post 1', 'Just some text', 'admin')
    DB.save(post)
    original_id = post.id
    DB.delete(post)
    assert DB._db['posts'][original_id] is None
    assert post.id is None


def test_cant_get_deleted_post():
    from xss_demo.models import (
        DB,
        Post,
        )

    post = Post('Post 1', 'Just some text', 'admin')
    DB.save(post)
    original_id = post.id
    DB.delete(post)

    with pytest.raises(ValueError):
        DB.get(Post, original_id)


def test_get_all_posts():
    from xss_demo.models import (
        DB,
        Post,
        )

    post = Post('Post 1', 'Just some text', 'admin')
    DB.save(post)
    saved_id = post.id

    all_posts = DB.get_all(Post)
    assert len(all_posts) >= 1
    assert any(post.id == saved_id for post in all_posts)


def test_post_creation_empty_list_comment_ids():
    from xss_demo.models import Post

    post = Post('Post 1', 'Just some text', 'admin')
    assert post.comment_ids == []


def test_save_comment_sets_id():
    from xss_demo.models import (
        DB,
        Comment,
        )

    comment = Comment('Just some text', 'admin', 0)
    assert comment.id is None
    DB.save(comment)
    assert comment.id is not None


def test_get_comment_returns_same_data():
    from xss_demo.models import (
        DB,
        Comment,
        )

    comment = Comment('Just some text', 'admin', 0)
    DB.save(comment)
    comment2 = DB.get(Comment, comment.id)
    assert comment is not comment2  # different objects
    assert comment.__dict__ == comment2.__dict__


def test_get_comment_invalid_id():
    from xss_demo.models import (
        DB,
        Comment,
        )

    with pytest.raises(ValueError):
        DB.get(Comment, 99)


def test_save_existing_comment_writes_data():
    from xss_demo.models import (
        DB,
        Comment,
        )

    comment = Comment('Just some text', 'admin', 0)
    DB.save(comment)
    original_id = comment.id
    comment.message = 'Modified text'
    DB.save(comment)
    assert comment.id == original_id
    assert DB.get(Comment, original_id).message == 'Modified text'


def test_save_comment_invalid_id():
    from xss_demo.models import (
        DB,
        Comment,
        )

    comment = Comment('Just some text', 'admin', 0)
    comment.id = 99
    with pytest.raises(ValueError):
        DB.save(comment)


def test_delete_comment():
    from xss_demo.models import (
        DB,
        Comment,
        )

    comment = Comment('Just some text', 'admin', 0)
    DB.save(comment)
    original_id = comment.id
    DB.delete(comment)
    assert DB._db['comments'][original_id] is None
    assert comment.id is None


def test_cant_get_deleted_comment():
    from xss_demo.models import (
        DB,
        Comment,
        )

    comment = Comment('Just some text', 'admin', 0)
    DB.save(comment)
    original_id = comment.id
    DB.delete(comment)

    with pytest.raises(ValueError):
        DB.get(Comment, original_id)


def test_get_all_comments():
    from xss_demo.models import (
        DB,
        Comment,
        )

    comment = Comment('Just some text', 'admin', 0)
    DB.save(comment)
    saved_id = comment.id

    all_comments = DB.get_all(Comment)
    assert len(all_comments) >= 1
    assert any(comment.id == saved_id for comment in all_comments)

