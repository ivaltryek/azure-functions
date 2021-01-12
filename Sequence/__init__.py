import azure.functions as func
import azure.durable_functions as df
import logging

def orchestrator_function(context: df.DurableOrchestrationContext):
    name = context.get_input()
    result1 = yield context.call_activity('SayHello', name)
    result2 = yield context.call_activity('SayHello', "Microsoft!")
    result3 = yield context.call_activity('SayHello', "Azure!")
    return [result1]

main = df.Orchestrator.create(orchestrator_function)