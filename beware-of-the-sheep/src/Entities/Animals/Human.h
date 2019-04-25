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
		inline std::string getSymbol() const override { return "HM"; }
		inline Kind getKind() const override { return Kind::Human; }
		inline std::string getClassName() const override { return "Human"; }
	private:
		static const unsigned int SPECIAL_SKILL_DURATION = 5;
		static const unsigned int SPECIAL_SKILL_COOLDOWN = 5;
		bool m_isSpecialSkillOn = false;
		unsigned int m_specialSkillDurationTimer = 0;
		unsigned int m_specialSkillCooldownTimer = 0;
	};

} // namespace bots
