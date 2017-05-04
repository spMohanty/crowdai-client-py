from base_challenge import BaseChallenge

class GeccoOptimizationChallenge2017Error(Exception):
    pass

class GeccoOptimizationChallenge2017(BaseChallenge):
    def __init__(self, api_key, config):
        self.challenge_id = "GeccoOptimizationChallenge2017"
        super(GeccoOptimizationChallenge2017, self).__init__(self.challenge_id, api_key, config)
        self._connect()
        self._authenticate()

    def _on_evaluate_response(self, args):
        print "Evaluate Response : ",args
        #TO-DO: Do Progress handling here
        if args["status"] == True:
            self.evaluation_response = args
        else:
            # TO-DO: Log Challenge Error
            raise GeccoOptimizationChallenge2017Error(args["message"])


    def evaluate(self, data, dry_run=False):
        self.evaluation_response = None
        self.socketio.emit('execute_function',
                        {   "session_token": self.session_key,
                            "challenge_id": self.challenge_id,
                            "function_name": "evaluate",
                            "data": data,
                            "dry_run" : dry_run
                        }, self._on_evaluate_response)
        self.socketio.wait_for_callbacks(seconds=self.config['challenges'][self.challenge_id]["TIMEOUT_EXECUTION"])
        if self.evaluation_response == None:
            raise GeccoOptimizationChallenge2017Error("Evaluation Request Timeout")
            # print "Evaluation Request Timed Out..."
        else:
            return self.evaluation_response

    def submit(self, data, dry_run=False):
        #Submit final score
        # Close socket.io connection
        pass
