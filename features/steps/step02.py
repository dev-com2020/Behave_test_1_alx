from behave import given, when, then

from blender import Blender


@given('I put "{thing}" in a blender')
def step_put_thing_into_blender(context, thing):
    context.blender = Blender()
    context.blender.add(thing)


@when('I switch the blender on')
def step_when_switch_blender_on(context):
    context.blender.switch_on()


@then('it should transform into "{other_thing}"')
def step_then_should_transfrom(context, other_thing):
    assert context.blender.result == other_thing
