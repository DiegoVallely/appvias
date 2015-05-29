

PreRelease = db.define_table("candidate",
	Field("emal", requires=[IS_NOT_EMPTY(),
							IS_EMAIL(error_message="Invalid Email")]))