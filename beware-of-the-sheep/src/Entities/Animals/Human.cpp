#include "pch.h"
#include "Human.h"
#include "World.h"

namespace bots {

	Human::Human(World & world, const Point & position) :
		Animal(world, position, 5, 4)
	{}

	void Human::action()
	{
		std::string message;

		int x = _getch();
		while (x == 32) {
			if (m_specialSkillCooldownTimer == 0 && !m_isSpecialSkillOn) {
				m_isSpecialSkillOn = true;
				message = "Special skill was activated.";
				m_world.addMessage(std::move(message));
			}

			x = _getch();
		}

		if (m_isSpecialSkillOn) {
			message = "Special skill will be on for " + std::to_string(SPECIAL_SKILL_DURATION - m_specialSkillDurationTimer) + " turns.";
			m_world.addMessage(std::move(message));
			++m_specialSkillDurationTimer;
		}

		if (m_specialSkillDurationTimer >= SPECIAL_SKILL_DURATION) {
			m_isSpecialSkillOn = false;
			m_specialSkillCooldownTimer = SPECIAL_SKILL_COOLDOWN;
			m_specialSkillDurationTimer = 0;
			message = "Special skill was deactivated.";
			m_world.addMessage(std::move(message));
		}

		if (m_specialSkillCooldownTimer > 0) {
			message = "Special skill can't be used for " + std::to_string(m_specialSkillCooldownTimer) + " turns.";
			m_world.addMessage(std::move(message));
			--m_specialSkillCooldownTimer;
		}

		if (x == 224) {
			int d = _getch();
			if (d == 72)
				move(0, -1);
			else if (d == 80)
				move(0, 1);
			else if (d == 75)
				move(-1, 0);
			else if (d == 77)
				move(1, 0);
		}
	}

} // namespace bots
