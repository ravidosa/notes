from hypothesis import given
from hypothesis import strategies as st
import pytest

z = st.integers()
t = st.text()
lt = st.lists(t, min_size=1)

class User:
    def __init__(self, name, age, friends=None):
        self.name = name
        self.age = age
        if friends is None:
            friends = []
        self.friends = friends

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name \
            and self.age == other.age \
            and self.friends == other.friends

@given(t, z, st.one_of(lt, st.none()))
def test_user_init(name, age, friends):
    user = User(name, age, friends)
    assert user.name == name and user.age == age and user.friends == (friends if friends else [])

def to_csv(user):
    return f"{user.name},{user.age}"

def from_csv(csv):
    name, age = csv.split(",")
    return User(name, int(age))

@given(t, z)
def test_serialize_deserialize(name, age):
    user = User(name, age)
    assert from_csv(to_csv(user)) == user

@pytest.mark.xfail(reason="The implementation is buggy")
@given(t, z)
def test_deserialize_serialize(name, age):
    csv = f"{name},{age}"
    assert to_csv(from_csv(csv)) == csv

def from_csv(csv):
    name, age = csv.rsplit(",", 1)
    return User(name, int(age))

def print_user(self):
    friends_str = " ".join(self.friends)
    print(f"INFO: User {self.name} is {self.age} years old and has friends: {friends_str}")

@given(t, z, lt)
def test_print_user(name, age, friends):
    user = User(name, age, friends)
    assert print_user(user) == None

def has_friend(self, other):
    return other.name in self.friends and self.name in other.friends

@given(t, z, lt, t, z, lt)
def test_has_friend(name1, age1, friends1, name2, age2, friends2):
    user1 = User(name1, age1, friends1)
    user2 = User(name2, age2, friends2)
    assert has_friend(user1, user2) == has_friend(user2, user1)

def server_response():
    return None

def user_from_server():
    response = None
    while response is None:
        response = server_response()

    name, age, friends = response.split(",")
    return User(name, int(age), friends.split(","))

@pytest.mark.skip()
def test_user_from_server():
    user = user_from_server()
    assert user is not None

def add_friend(self, other):
    self.friends = [other.name]

@given(t, z, t, z)
def test_add_friend(name1, age1, name2, age2):
    user1 = User(name1, age1)
    user2 = User(name2, age2)
    add_friend(user1, user2)
    assert user1.friends == [user2.name]

def update_age_with(self, f):
    return User(self.name, f(self.age), self.friends)

@pytest.mark.xfail("The function is not pure")
@given(t, z, st.functions(like=lambda x: x,returns=st.integers()))
def test_update_age_with_1(name, age, f):
    user = User(name, age)
    user_update = update_age_with(user, f)
    assert user_update.age == f(age)

@given(t, z, st.functions(like=lambda x: x,returns=st.integers(), pure=True))
def test_update_age_with_2(name, age, f):
    user = User(name, age)
    user_update = update_age_with(user, f)
    assert user_update.age == f(age)

@given(t, z, st.functions(like=lambda x: x,returns=st.integers()))
def test_update_age_with_3(name, age, f):
    track = []
    def track_f(age_):
        track.append(f(age_))
        return track[-1]
    
    user = User(name, age)
    user_update = update_age_with(user, track_f)
    assert user_update.age == track[0]