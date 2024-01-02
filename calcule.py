class Calcul:
    
    def __init__(self):
        pass  

    def factorielle(self, n):
        if n == 0 or n ==1 :
            return 1
        else:
            return n * self.factorielle(n - 1)

    def somme(self, n):
        return sum(range(1, n + 1))
    
    def testPrim(self, nbr):
        n3=0
        for i in range(1,nbr+1):
            if(nbr%i==0):
                n3 = n3 + 1
        if(n3 == 2):
            return True
        else:
            return False
    
        n3=0
        for i in range(1,nbr+1):
            if(nbr%i==0):
                n3 = n3 + 1
        if(n3 == 2):
            return True
        else:
            return False
    def table_mult(self, n):
        for i in range(1, 11):
            print(f"{n} * {i} = {n * i}")

    def all_tables_mult(self):
        for i in range(1, 10):
            self.table_mult(i)
            
    def listdiv(self, n):
        return [ i for i in range(1, n + 1) if n % i == 0]

    def listdivprim(self, n):
        return [ i for i in range(1, n + 1) if n % i == 0 and self.testPrim(i)]


c= Calcul()

print(c.factorielle(3))

print( c.somme(5))

print("Est-ce que 7 est premier ?", c.testPrim(7))

print("Table de multiplication de 6:")
c.table_mult(6)

print("Tables de multiplication de 1 à 9:")
c.all_tables_mult()

print("Liste des diviseurs de 5 :", c.listdiv(5))

print("Liste des diviseurs premiers de 15 :", c.listdivprim(15))

