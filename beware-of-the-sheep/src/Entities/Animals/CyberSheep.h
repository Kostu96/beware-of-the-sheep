#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class CyberSheep :
		public Animal
	{
	public:
		CyberSheep(World & world, const Point & position);
		virtual ~CyberSheep() = default;

		void action() override;
		void collision(const Entity & other) override;
	protected:
		inline const char * getSymbol() const override { return "CP"; }
	private:

	};

} // namespace bots
