## List of places I want to Visit

want_to_visit_places=["kashmir","paris","california","bhutan"]

##Temporary sorted list in alphabetical order

print(want_to_visit_places)
print(sorted(want_to_visit_places))

##print the original list

print(want_to_visit_places)

## Print list in reverse order without actually changing the list
print(sorted(want_to_visit_places,reverse=True))

#Original list is still intact
print(want_to_visit_places)

##Reverse the order of list permenantly
want_to_visit_places.reverse()

print(want_to_visit_places)

## Make the list order back to original
want_to_visit_places.reverse()

print(want_to_visit_places)

## sort the list in alphabetical order
want_to_visit_places.sort()
print(want_to_visit_places)

## sort the list in reverse alphabetical order
want_to_visit_places.sort(reverse=True)
print(want_to_visit_places)