#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Wolf :
		public Animal
	{
	public:
		Wolf(World & world, const Point & position);
		virtual ~Wolf() = default;
	protected:
		inline std::string getSymbol() const override { return "WF"; }
		inline Kind getKind() const override { return Kind::Wolf; }
		inline std::string getClassName() const override { return "Wolf"; }
	private:

	};

} // namespace bots
