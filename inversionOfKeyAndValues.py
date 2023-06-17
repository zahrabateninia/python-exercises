def groups_per_user(group_dictionary):
	user_groups = {}
	for groupName, users in group_dictionary.items():
		for user in users:
			if user in user_groups:
				user_groups[user].append(groupName)
			else:
				user_groups[user] = [groupName]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
#output: {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}
