from flask import Flask, request, jsonify
from waitress import serve
# from flask_json import FlaskJSON, JsonError, json_response, as_json
from urllib.parse import urlparse
import re
import hashlib
import os
import tldextract
import dill as pickle
import numpy as np

app = Flask(__name__)

path_name = 'C:/Users/AMARA NYANZI/OneDrive/Desktop/Machine Learning/SavedModel/fifthy.pkl'
with open(path_name, 'rb') as file:
    data = pickle.load(file)


@app.route('/home', methods=['GET','POST'])
def checkers():

    url_data = request.get_json(force=True)
    url = url_data['input']


    # return jsonify({'count_forwardslash': forward,
    #                 'count_questionmark': question,
    #                 'count_percent': percent})


    xgb_c = data["model"]
    # xgb_c.predict(url)
    urlparse = data["urlparse"]
    urlparse = urlparse
    tldextract = data["tldextract"]
    tldextract = tldextract
    get_tld = data["get_tld"]
    get_tld = get_tld
    hashlib = data["hashlib"]
    hashlib = hashlib
    os = data["os"]
    os = os
    re = data["re"]
    re = re
    abnormal_url = data["abnormal"]
    abnormal_url = abnormal_url(url)
    suspicious_words = data["sus_url"]
    suspicious_words = suspicious_words(url)
    count_https = data["https"]
    count_https = count_https(url)
    count_www = data["www"]
    count_www = count_www(url)
    url_length = data["url_length"]
    url_length = url_length(url)
    hostname_length = data["host_length"]
    hostname_length = hostname_length(url)
    count_percent = data["percent"]
    count_percent = count_percent(url)
    fd_length = data["fd_length"]
    fd_length = fd_length(url)
    count_questionmark = data["question"]
    count_questionmark = count_questionmark(url)
    count_forwardslash = data["forwardslash"]
    count_forwardslash = count_forwardslash(url)
    count_equals = data["equals"]
    count_equals = count_equals(url)
    count_hyphen = data["hyphen"]
    count_hyphen = count_hyphen(url)
    letter_count = data["letters"]
    letter_count = letter_count(url)
    digit_count = data["digits"]
    digit_count = digit_count(url)
    shortening_service = data["short_service"]
    shortening_service = shortening_service(url)
    no_of_embed = data["embedded"]
    no_of_embed = no_of_embed(url)
    having_ip_address = data["ip_address"]
    having_ip_address = having_ip_address(url)
    count_non_alphanumeric = data["non_alpha"]
    count_non_alphanumeric = count_non_alphanumeric(url)
    tld_length = data["tld"]
    tld_length = tld_length(url)
    extract_file_type = data["file"]
    extract_file_type = extract_file_type(url)
    extract_root_domain = data["root_domain"]
    extract_root_domain = extract_root_domain(url)
    extract_tld = data["tld"]
    extract_tld = extract_tld(url)
    count_attherate = data["rate"]
    count_attherate = count_attherate(url)
    extract_rooty = data['rooty']
    extract_rooty = extract_rooty(url)

    status = [abnormal_url, suspicious_words, count_https, count_www, url_length, hostname_length, count_percent, fd_length,
              count_questionmark, count_forwardslash, count_equals, count_hyphen, letter_count, digit_count, shortening_service,
              no_of_embed, having_ip_address, count_non_alphanumeric, tld_length, extract_root_domain, extract_file_type,
              extract_tld, count_attherate, extract_rooty]

    def get_prediction_from_url():
        features_test = status
        features_test = np.array(features_test, dtype=object).reshape((1, -1))

        pred = xgb_c.predict(features_test)
        if int(pred[0]) == 0:

            res = "SAFE"
            return res
        elif int(pred[0]) == 1.0:

            res = "DEFACEMENT"
            return res
        elif int(pred[0]) == 2.0:
            res = "PHISHING"
            return res

        elif int(pred[0]) == 3.0:

            res = "MALWARE"
            return res

    result = get_prediction_from_url()

    if result == 'SAFE':
        test = ('The URL is ' + result + ' :four_leaf_clover: . Proceed with browsing.')
    elif result == 'DEFACEMENT':
        test = ('The URL is most likely ' + result + '⚠️. Please proceed with browsing.')
    elif result == 'PHISHING':
        test = ('The URL is most likely ' + result + '⚠️. Please proceed with browsing.')
    elif result == 'MALWARE':
        test = ('The URL is most likely ' + result + ' ⚠️. Please reconsider visiting this site.')
    else:
        test = ('Hmm, something went wrong. Please try again.')

    return jsonify({'prediction': test})

@app.route('/api')
def nix():
    return 'Wait a minute'

mode = "dev"

if __name__ == '__main__':
    if mode =="dev":
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        serve(app, host='0.0.0.0', port=5000)