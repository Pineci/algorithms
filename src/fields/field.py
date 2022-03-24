from typing import Optional, Union, List
from sympy.ntheory import factorint
from sympy import Symbol, Poly
from sympy.polys.agca.extensions import FiniteExtension

# Check this article on how to compute Conway polynomials, a lexigraphically
# ordered set of irreducible polynomials:
# http://www.math.rwth-aachen.de/~Frank.Luebeck/data/ConwayPol/index.html

## TODO: Look into sympy instead to use FiniteFields. Look into FieldExtensions

class FiniteField:
    
    def __init__(self, order: Optional[int]=None, prime: Optional[int]=None, power: int=1, value: Union[int, List[int]]):
        '''
        

        Args:
            value (int, List[int]): The value of the element in the finite field. Elements are specified in order
                                    of increasing significance, i.e. if x is a root of an irreducible polynomial
                                    in the field GF(p^3), then the list [a0, a1, a2] corresponds to the element
                                    a0 + a1*x + a2*(x**2)

        Returns:
            

        Raises:
            
        '''

        # Make sure field is specified correctly
        if order is None and prime is None:
            raise ValueError("The arguments 'order' and 'prime' cannot both be None! Please specify exactly one parameter.")
        if order is not None and prime is not None:
        #    raise ValueError("The arguments 'order' and 'prime' cannot both be specified! Please specify exactly one parameter.")
            if not order == (prime ** power):
                raise ValueError("Found an inconsistency in field specification! Please ensure that order == prime ** power.")
                self.prime = prime
                self.power = power
                self.order = order
        if order is None:
            self.prime = prime
            self.power = power
            self.order = prime ** power
        if prime is None:
            factorization = factorint(order)
            if len(factorization) > 1:
                raise ValueError("Finite fields must have a size which is a prime power! Please specify a different field size.")
            self.prime = list(factorization.keys())[0]
            self.power = factorization[self.prime]
            self.order = order
        
        
        # Make sure field value is specified correctly
        if self.power > 1:
            if isinstance(value, int):
                raise ValueError("When a finite field is a non-prime field, please specify the value using a list.")


    def convert_list_to_poly(self, coefs, modulus):
        x = Symbol('x')
        return Poly.from_list(coefs[::-1], x, modulus=modulus)

    # TODO: Implement this
    def test_is_primitive(self, )



    


