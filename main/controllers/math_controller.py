from decimal import Decimal
from unicodedata import decimal, numeric
from flask import request, Response,jsonify
from flask_restx import Resource,Namespace

from ..utils.file_logger import error
from ..utils.decorators import authorize
from ..service.math_service import calculate_min,calculate_max,calculate_average,calculate_median,calculate_percentile

maths_api=Namespace("Maths","Maths")

@maths_api.route('/min')
class Min(Resource):
    @maths_api.response(200,'Success')
    @maths_api.response(400,'Bad Request')
    @maths_api.response(500,'Inernal Server Error')
    @maths_api.response(401,'Unauthorized')
    @maths_api.response(500,'Internal Server Error')
    @maths_api.doc(params={'list_of_numbers': {'description':'comma seperated list of numbers','required':True}})
    @maths_api.doc(params={'quantifier': {'description':'quantifier (how many)','type':'int','required':True}})
    @authorize
    def get(self):
        listOfNumbers=request.args.get('list_of_numbers')
        quantifier=request.args.get('quantifier')

        if listOfNumbers is None or quantifier is None:
            return Response("list_of_numbers and quantifier can't be empty",400)
        
        if not quantifier.isdigit():
            return Response("quantifer should be a number",400)

        try:
            listOfNumbers_list=[int(x) for x in listOfNumbers.split(',') if x.isnumeric()]
            quantifier=int(quantifier)

            n_minimum_numbers = calculate_min(listOfNumbers_list,quantifier)

            return jsonify(mins=n_minimum_numbers)
        except Exception as e:
            error(str(e))
            return Response(str(e),500)


@maths_api.route('/max')
class Max(Resource):
    @maths_api.response(200,'Success')
    @maths_api.response(400,'Bad Request')
    @maths_api.response(401,'Unauthorized')
    @maths_api.response(500,'Internal Server Error')
    @maths_api.response(500,'Inernal Server Error')
    @maths_api.doc(params={'list_of_numbers': {'description':'comma seperated list of numbers','required':True}})
    @maths_api.doc(params={'quantifier': {'description':'quantifier (how many)','type':'int','required':True}})
    @authorize
    def get(self):
        listOfNumbers=request.args.get('list_of_numbers')
        quantifier=request.args.get('quantifier')
        
        if listOfNumbers is None or quantifier is None:
            return Response("list_of_numbers and quantifier can't be empty",400)
        
        if not quantifier.isdigit():
            return Response("quantifer should be a number",400)
        try:
           listOfNumbers_list=[int(x) for x in listOfNumbers.split(',') if x.isnumeric()]
           quantifier=int(quantifier)

           n_maximum_numbers= calculate_max(listOfNumbers_list,quantifier)

           return jsonify(maxs=n_maximum_numbers)
        except Exception as e:
            error(str(e))
            return Response(str(e),500)

@maths_api.route('/average')
class Average(Resource):
    @maths_api.response(200,'Success')
    @maths_api.response(400,'Bad Request')
    @maths_api.response(500,'Inernal Server Error')
    @maths_api.response(401,'Unauthorized')
    @maths_api.response(500,'Internal Server Error')
    @maths_api.doc(params={'list_of_numbers': {'description':'comma seperated list of numbers','required':True}})
    @authorize
    def get(self):
        listOfNumbers=request.args.get('list_of_numbers')
        
        if listOfNumbers is None or len(listOfNumbers) ==0:
            return Response("list_of_numbers should have atleast one number",400)
        
        try:
           listOfNumbers_list=[int(x) for x in listOfNumbers.split(',') if x.isnumeric()]
           average_n= calculate_average(listOfNumbers_list)

           return jsonify(average=average_n)
        except Exception as e:
            error(str(e))
            return Response(str(e),500)

@maths_api.route('/median')
class Median(Resource):
    @maths_api.response(200,'Success')
    @maths_api.response(400,'Bad Request')
    @maths_api.response(500,'Inernal Server Error')
    @maths_api.response(401,'Unauthorized')
    @maths_api.response(500,'Internal Server Error')
    @maths_api.doc(params={'list_of_numbers': {'description':'comma seperated list of numbers','required':True}})
    @authorize
    def get(self):
        listOfNumbers=request.args.get('list_of_numbers')
        
        if listOfNumbers is None or len(listOfNumbers) ==0:
            return Response("list_of_numbers should have atleast one number",400)
        
        try:
           listOfNumbers_list=[int(x) for x in listOfNumbers.split(',') if x.isnumeric()]
           median_n= calculate_median(listOfNumbers_list)

           return jsonify(median=median_n)
        except Exception as e:
            error(str(e))
            return Response(str(e),500)

@maths_api.route('/percentile')
class Min(Resource):
    @maths_api.response(200,'Success')
    @maths_api.response(400,'Bad Request')
    @maths_api.response(500,'Inernal Server Error')
    @maths_api.response(401,'Unauthorized')
    @maths_api.response(500,'Internal Server Error')
    @maths_api.doc(params={'list_of_numbers': {'description':'comma seperated list of numbers','required':True}})
    @maths_api.doc(params={'quantifier': {'description':'quantifier (qth percentatile)','type':'decimal','required':True}})
    @authorize
    def get(self):
        listOfNumbers=request.args.get('list_of_numbers')
        quantifier=request.args.get('quantifier')

        if listOfNumbers is None or quantifier is None:
            return Response("list_of_numbers and quantifier can't be empty",400)
        
        if not quantifier.isnumeric():
            return Response("quantifer should be a number",400)       
        try:
            listOfNumbers_list=[numeric(x) for x in listOfNumbers.split(',') if x.isnumeric()]
            quantifier=float(quantifier)

            percentage = calculate_percentile(listOfNumbers_list,quantifier)
            
            return jsonify(percentile=percentage)
        except Exception as e:
            error(str(e))
            return Response(str(e),500)
