from behave import given, when, then

from blender import Blender


@given('I put "{things}" in a blenders')
def step_put_thing_into_blender(context, things):
    context.blender = Blender()
    context.blender.add(things)


@when('I switch the blender on!')
def step_when_switch_blender_on(context):
    context.blender.switch_on()


@then('it should transform into "{other_things}!"')
def step_then_should_transfrom(context, other_things):
    assert context.blender.result == other_things
