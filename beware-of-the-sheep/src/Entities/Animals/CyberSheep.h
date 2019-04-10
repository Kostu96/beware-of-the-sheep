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
		inline Kind getKind() const override { return Kind::CyberSheep; }
	private:

	};

} // namespace bots
