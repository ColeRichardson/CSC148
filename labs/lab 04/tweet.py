from __future__ import annotations  # Reference: Reading on Type Annotations

from datetime import date  # Python library for working with dates (and times)
from typing import List    # Python library for expressing complex types

class Tweet:
    """A tweet, like in Twitter.

    === Attributes ===
    content: the contents of the tweet.
    userid: the id of the user who wrote the tweet.
    created_at: the date the tweet was written.
    likes: the number of likes this tweet has received.
    """
    content: str
    userid: str
    created_at: date
    likes: int

    def __init__(self, who: str, when: date, what: str) -> None:
        """Initialize a new Tweet.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.userid
        'Rukhsana'
        >>> t.created_at
        datetime.date(2017, 9, 16)
        >>> t.content
        'Hey!'
        >>> t.likes
        0
        """

        # YOUR CODE HERE
        self.content = what
        self.userid = who
        self.created_at = when
        self.likes = 0

    def like(self, n: int) -> None:
        """Record the fact that this tweet received <n> likes.

        These likes are in addition to the ones <self> already has.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.like(3)
        >>> t.likes
        3
        """

        # YOUR CODE HERE
        self.likes += 1

    def edit(self, new_content: str) -> None:
        """Replace the contents of this tweet with the new message.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.edit('Rukhsana is cool')
        >>> t.content
        'Rukhsana is cool'
        """

        # YOUR CODE HERE
        self.content = new_content


class User:
    """A Twitter user.

    === Attributes ===
    userid: the userid of this Twitter user.
    bio: the bio of this Twitter user.
    tweets: the tweets that this user has made.
    """
    # Attribute types
    userid: str
    bio: str
    tweets: List[Tweet]

    def __init__(self, id_: str, bio: str) -> None:
        """Initialize this User.

        >>> david = User('David', 'is cool')
        >>> david.tweets
        []
        """

        # YOUR CODE HERE
        self.userid = id_
        self.bio = bio
        self.tweets = []

    def tweet(self, message: str) -> None:
        """Record that this User made a tweet with the given content.

        Use date.today() to get the current date for the newly created tweet.
        """

        # YOUR CODE HERE
        tweet = Tweet(self.userid, date.today(), message)
        self.tweets.append(tweet)

