from Updated_Patient_Class import Encounter, Patient


# make a new patient
bob = Patient("Bob", ...)
mary = Patient("Mary", ...)

# make some encounters
bob.add_encounter(Encounter(90, "May 22"))
mary.add_encounter(Encounter(67, "Apr 15"))
mary.add_encounter(Encounter(68, "May 23"))

def find_encounters_for(patient):
    return patient.encounters

bobs_encounters = find_encounters_for(bob)
print bobs_encounters # >>> [Encounter(Bob, 90, May 22)]

marys_encounters = find_encounters_for(mary)
print marys_encounters # >>> [Encounter(Mary, 67, Apr 15), Encounter(Mary, 68, May 23)]