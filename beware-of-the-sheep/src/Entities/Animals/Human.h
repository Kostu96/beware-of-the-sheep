#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Human :
		public Animal
	{
	public:
		Human(World & world, const Point & position);
		virtual ~Human() = default;

		void action() override;
		// TODO: add collision
	protected:
		inline const char * getSymbol() const override { return "HM"; }
		inline Kind getKind() const override { return Kind::Human; }
		inline const char * getClassName() const override { return "Human"; }
	private:

	};

} // namespace bots
