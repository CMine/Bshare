var postSignUp = function(userId, info){
	if(info.profile.admin_code == '123'){
		Roles.addUsersToRoles(userId, ['normal-user', 'admin', info.profile.admin_code]);
	}
	else{
		Roles.addUsersToRoles(userId, ['normal-user', info.profile]);
	}
}

AccountsTemplates.configure({
	postSignUpHook: postSignUp
});
