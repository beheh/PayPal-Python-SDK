# This class was generated on Sun, 08 Apr 2018 16:12:12 UTC by version 0.1.0-dev+291f3f of Braintree SDK Generator
# dispute_get_request.py
# @version 0.1.0-dev+291f3f
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class DisputeGetRequest:
    """
    Shows details for a dispute, by ID.<blockquote><strong>Note:</strong> The fields that appear in the response depend on whether you access this call through first- or third-party access. For example, if the merchant shows dispute details through third-party access, the customer's email ID does not appear.</blockquote>
    """
    def __init__(self, dispute_id):
        self.verb = "GET"
        self.path = "/v1/customer/disputes/{dispute_id}?".replace("{dispute_id}", quote(str(dispute_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
