'''
    Classes
        instances
        constructor
        attributes
        methods
        inheritances
'''

class Disease(object):
    def __init__(self, name, i_rate = 1, strands=[]):
        self.name = name
        self.strand_type = []
        self.infection_rate = i_rate

    def infect(self, infection_number):
        self.infection_rate *= infection_number
        return self
    def updates_strands(self, **args):
        # 
corona = Disease('Corona')
print(corona.name)
print(corona.infection_rate)
corona.strand_one = "kasjdflh"

# infect(10)
method_result = corona.infect(10).infect(10)
print(method_result)

print(corona.infection_rate)
swineFlu = Disease('Swine Flu', 50)
print(swineFlu.name)
print(swineFlu.infection_rate)