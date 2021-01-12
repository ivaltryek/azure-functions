import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    result1 = yield context.call_activity('SayHello', "World!")
    result2 = yield context.call_activity('SayHello', "Microsoft!")
    result3 = yield context.call_activity('SayHello', "Azure!")
    return [result1, result2, result3]

main = df.Orchestrator.create(orchestrator_function)