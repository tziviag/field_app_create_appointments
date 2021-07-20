from main import main
def handler(event, context):
    try:
        main()
        print('start this app')
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )
