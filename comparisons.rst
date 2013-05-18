=====================================
 More advanced attribute comparisons
=====================================

Axiom provides a few tools for more advanced querying patterns.

.. testsetup::

    from axiom.store import Store
    from person import Person

Checking if something is part of a fixed set
============================================

A common pattern is trying to find all items where some attribute is a
member (or not a member) of some fixed set. Axiom provides ``oneOf``
and ``notOneOf`` for this.

To demonstrate this, let's create a store with some people in it:

.. doctest::

   >>> store = Store()
   >>> alice = Person(store=store, name=u"Alice")
   >>> bob = Person(store=store, name=u"Bob")
   >>> carol = Person(store=store, name=u"Carol")


There's a secret club for people who like ice cream with peanut butter
flavors. The member's list only has two names on it: Alice and Bob.

.. doctest::

   >>> secretClubMemberNames = [u"Alice", u"Bob"]

We can create a comparison, which we'll call ``inSecretClub``, that
checks if a person's name is in the list of secret club member names.

.. doctest::

   >>> inSecretClub = Person.name.oneOf(secretClubMemberNames)
   >>> list(store.query(Person, inSecretClub, sort=Person.name.ascending))
   [Person(name=u'Alice', storeID=1)@..., Person(name=u'Bob', storeID=2)@...]

Additionally, there's a super secret club for people who like coconut
flavored ice cream. Both Bob and Carol like coconut flavored ice
cream. If we want to query all the people who *don't*, we'd use
``notOneOf``:

.. doctest::

   >>> doesntLikeCoconut = Person.name.notOneOf([u"Bob", u"Carol"])
   >>> list(store.query(Person, doesntLikeCoconut))
   [Person(name=u'Alice', storeID=1)@...]

And that's all there is to it.

``notOneOf`` and ``oneOf`` are supported by almost all attributes
(except ``inmemory``, since that's inherently unqueryable). That said,
comparing floats (``ieee754_double``) is probably not what you wanted
-- but that's inherent to floats, not anything specific to Axiom.
