#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Turtle :
		public Animal
	{
	public:
		Turtle(World & world, const Point & position);
		virtual ~Turtle() = default;

		void action() override;
		void collision(Entity & other) override;
		bool dodgedAttack(unsigned int strength) const override { return strength < 5; }
	protected:
		inline std::string getSymbol() const override { return "TT"; }
		inline Kind getKind() const override { return Kind::Turtle; }
		inline std::string getClassName() const override { return "Turtle"; }
	};

} // namespace bots
