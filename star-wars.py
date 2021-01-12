lukes_relatives = {}
lukes_relatives['darth_vader'] = "father"
lukes_relatives['leia'] = "sister"
lukes_relatives['han'] = "brother in law"
lukes_relatives['r2d2'] = "droid"


def determine_if_entry_is_lukes_relative(entry):
    print(lukes_relatives[entry])


determine_if_entry_is_lukes_relative("darth_vader")
determine_if_entry_is_lukes_relative("leia")
determine_if_entry_is_lukes_relative("han")
determine_if_entry_is_lukes_relative("r2d2")
